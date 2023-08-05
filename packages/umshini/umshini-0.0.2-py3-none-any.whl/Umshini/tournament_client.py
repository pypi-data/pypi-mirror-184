import socket
import json
import gymnasium as gym
import numpy as np
from Umshini.utils.socket_wrap import SocketWrapper
from Umshini.utils.compress import decompress
from Umshini.envs import make_test_env, all_environments
from colorama import Fore, Style
from halo import Halo


# Send JSON through socket
def send_json(sock, data):
    return sock.sendall(json.dumps(data).encode("utf-8"))


# Receive JSON from socket
def recv_json(sock, timeout=30):
    sock.settimeout(timeout)
    data = sock.recv(2 ** 30)  # Arbitrarily large buffer
    sock.settimeout(30)
    return data


class NetworkEnv(gym.Env):
    def __init__(self, env_id, seed, game_ip, game_port, username, token):
        self.game_connection = SocketWrapper(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        )
        # Create game server connection
        self.game_connection.connect((game_ip, game_port))
        send_json(self.game_connection, {"username": username, "token": token})
        self.game_data = recv_json(self.game_connection)
        self.terminated = self.game_data["type"] == "terminate"

        # Create env for initial action and observation spaces
        self.env, self.turn_based = make_test_env(env_id, seed=seed)
        self.agent = agent = (
            self.game_data["agent"] if not self.terminated else self.env.possible_agents[0]
        )
        self.observation_space = self.env.observation_space(agent)
        self.action_space = self.env.action_space(agent)
        self.action_space.seed(seed)
        self.obs = None

    def step(self, action):
        if self.terminated:
            print("terminated before single step occurred!")
            return self.obs, 0, True, True, {}

        # Convert Numpy types to Python types
        if hasattr(action, "dtype"):
            action = action.item()

        # Send action to game server
        assert (isinstance(action, int) or
                isinstance(action, float) or
                isinstance(action, str) or
                isinstance(action, dict) or
                isinstance(action, list)), "Action is not a valid type."
        assert self.action_space.contains(action), "Action not in action space."

        act_data = {"type": "action", "action": action}
        send_json(self.game_connection, act_data)

        # Receive observation from game server
        observation_data = recv_json(self.game_connection)
        if observation_data["type"] != "observation":
            # Game is done
            rew = 0
            term = True
            trunc = True
            info = {}
            info["_terminated"] = True
            return self.obs, rew, term, trunc, info

        # Unpack observation
        obs = decompress(observation_data["data"][self.agent])
        self.obs = obs

        # TODO: Decide what information a live tournament agent should have access to.
        # Probably observation, info, term or trunc, though term or trunc are obvious from the message type
        rew = 0
        info = {}
        term = False
        trunc = False
        return obs, rew, term, trunc, info

    def render(self, mode='human'):
        # TODO: Figure out appropriate behavior here. Probably rendering live on the website.
        return self.env.render(mode=mode)

    def reset(self):
        "Resetting mid-game would cause serious desync issues"
        return

    def close(self):
        self.env.close()
        self.game_connection.close()


# Local environment used to test if agent works before connecting to network env
class TestEnv(gym.Env):
    def __init__(self, env_id):
        seed = 1
        self.env, self.turn_based = make_test_env(env_id, seed=seed)
        self.env.reset()
        self.agent = agent = self.env.agents[0]
        self.observation_space = self.env.observation_space(agent)
        self.action_space = self.env.action_space(agent)
        self.num_steps = 0
        self.was_term = False
        self.was_trunc = False
        self.obss = None

    def reset(self):
        self.num_steps = 0
        self.was_term = False
        self.was_trunc = False
        obss = self.env.reset()
        return obss[self.agent]

    def step(self, action):
        assert not self.was_term and not self.was_trunc, "stepped after term or trunc, should terminate loop"

        # Set random actions for all other agents in parallel game or None in turn-based game
        actions = {
            agent: (None if self.turn_based else self.env.action_space(agent).sample()) for agent in self.env.agents
        }
        actions[self.env.aec_env.agent_selection] = action
        self.obss, rews, terms, truncs, infos = self.env.step(actions)

        if self.num_steps > 50:
            trunc = True
            term = True
        else:
            term = terms[self.agent]
            trunc = truncs[self.agent]

        obs = self.obss[self.agent]
        rew = rews[self.agent]
        info = infos[self.agent]

        self.was_term = term
        self.was_trunc = trunc
        self.num_steps += 1

        # Find next active agents
        if self.turn_based:
            active_agents = [self.env.unwrapped.agent_selection]
        else:
            active_agents = self.env.agents

        # Step again if testing agent is not next
        if not self.was_term and not self.was_trunc and self.agent not in active_agents:
            obs = self.obss[self.env.unwrapped.agent_selection]
            if (obs is not None
                and isinstance(obs, dict)
                and obs and "action_mask" in obs):
                action = np.random.choice(obs["action_mask"].nonzero()[0])
            else:
                action = self.env.action_space(self.env.unwrapped.agent_selection).sample()
            return self.step(action)
        else:
            return obs, rew, term, trunc, info

    def render(self, mode='human'):
        return


# Local environment used to test if agent works before connecting to network env
class TestAECEnv(gym.Env):
    def __init__(self, env_id):
        seed = 1
        self.env = make_test_env(env_id, seed=seed, turn_based=True)
        self.env.reset()
        self.agent = agent = self.env.agents[0]
        self.observation_space = self.env.observation_spaces[agent]
        self.action_space = self.env.action_spaces[agent]
        self.num_steps = 0
        self.was_term = False
        self.was_trunc = False

    def reset(self):
        self.num_steps = 0
        self.was_term = False
        self.was_trunc = False
        self.env.reset()

    def step(self, action):
        assert not self.was_term and not self.was_trunc, "stepped after term or trunc, should terminate loop"
        # Set random actions for all other agents
        self.env.step(action)
        if self.num_steps > 50:
            trunc = True
            term = True
        else:
            obs, rew, term, trunc, info = self.env.last()

        self.was_term = term
        self.was_trunc = trunc
        self.num_steps += 1

    def last(self):
        return self.env.last()

    def render(self, mode='human'):
        return


class TournamentConnection:
    def __init__(self, ip, port, botname, key, available_games):
        print("Connecting to matchmaker for following games: ", available_games)
        if available_games == ["__all__"]:
            available_games = list(all_environments.keys())

        self.botname = botname
        self.ip_address = ip
        self.port = int(port)
        self.key = key
        self.available_games = available_games
        self.main_connection = None  # Connection to tournament server
        self.tournament_completed = False
        self._test_environments()

    # Test agent in every game
    def _test_environments(self):
        for game in self.available_games:
            test_env = TestEnv(game)
            obs = test_env.reset()
            for _ in range(100):
                if (obs is not None
                    and isinstance(obs, dict)
                    and obs and "action_mask" in obs):
                    action = np.random.choice(obs["action_mask"].nonzero()[0])
                else:
                    action = test_env.action_space.sample()
                obs, _, term, trunc, _ = test_env.step(action)
                if term or trunc:
                    print("{} passed test in {}".format(self.botname, game))
                    break

    def _connect_game_server(self):
        # If tournament is over, return no environment
        if self.tournament_completed:
            return None

        # Receive game server info from matchmaker
        spinner = Halo(text='Waiting for players', text_color='cyan', color='green', spinner='dots')
        spinner.start()
        try:
            ready_data = recv_json(self.main_connection, timeout=60)
        except TimeoutError as err:
            print("Not enough players to start tournament.")
            raise err
        spinner.succeed()
        send_json(self.main_connection, {"type": "ready"})

        # Receive game server info from matchmaker
        spinner = Halo(text='Creating your game', text_color='cyan', color='green', spinner='dots')
        spinner.start()
        try:
            sdata = recv_json(self.main_connection)
        except TimeoutError as err:
            print("Failed to receive game info from server")
            raise err
        spinner.succeed()

        # Create network env with game server info
        env = NetworkEnv(
            sdata["env"],
            sdata["seed"],
            self.ip_address,
            sdata["port"],
            sdata["username"],
            sdata["token"],
        )
        return env

    # Start connection to matchmaking server
    def _setup_main_connection(self):
        self.main_connection = SocketWrapper(
            socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        )
        self.main_connection.connect((self.ip_address, self.port))
        send_json(
            self.main_connection,
            {
                "botname": self.botname,
                "key": self.key,
                "client_version": "1.0",
                "available_games": self.available_games,
            },
        )

        try:
            init_data = recv_json(self.main_connection)
        except TimeoutError as err:
            print("Failed to connect to matchmaker.")
            raise err

        # Handle connection errors
        if init_data["type"] == "bad_creds":
            raise RuntimeError("server did not accept credentials")
        if init_data["type"] == "bad_client_version":
            raise RuntimeError("Old client version. Please udpate your client to the latest version available.")
        if init_data["type"] == "connected_too_many_servers":
            raise RuntimeError("This user is already connected to the server too many times.")
        if init_data["type"] == "invalid_botname":
            raise RuntimeError(f"This user does not have a bot with the provided name ({self.botname})")
        if init_data["type"] != "connect_success":
            raise RuntimeError(f"Something went wrong during login: {init_data['type']}")

        # Check if tournament is complete
        if init_data["complete"]:
            self.tournament_completed = True

    # TODO: Implement terminate signal for tournament and receive it here
    def next_match(self):
        # Create tournament server connection if it does not already exist
        if self.main_connection is None:
            try:
                self._setup_main_connection()
            except Exception as e:
                raise e

        if self.tournament_completed:
            print(Fore.GREEN + "User: {} successfully completed tournament".format(self.botname))
        else:
            # Connect to game server
            print(Fore.GREEN + "User: {} successfully connected to Umshini".format(self.botname))
        print(Style.RESET_ALL)

        # Connect to game server
        game_env = self._connect_game_server()
        self.main_connection.close()
        self.main_connection = None
        return game_env
