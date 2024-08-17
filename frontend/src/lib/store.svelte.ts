import PlayState from "./enums/play_state";
import Services from "./enums/services";

import env from "./env";
import { getContext, setContext } from "svelte";

const USER_KEY = Symbol("USER");
const PLAYER_KEY = Symbol("PLAYER");

function rune<T>(init_value: T) {
  let value: T = $state(init_value);

  return {
    get value() {
      return value;
    },
    set value(v: T) {
      value = v;
    },
  };
}

class User {
	id: number = $state(0);
	owner: boolean = $state(false);
	party_id: number | null = $state(null);
	service: Services = $state(Services.SPOTIFY);
	token: string = $state("");
	username: string = $state("");
	logged: boolean = $state(false);

	async get_me(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + '/user/me', {
			method: 'GET',
			credentials: 'include',
		});
		if (response.status !== 200) {
			this.logged = false;
			return ;
		}
		const response_json = (await response.json())['user'];
		this.id = response_json['id'];
		this.party_id = response_json['party_id'];
		this.service = response_json['service'];
		this.token = response_json['token'];
		this.username = response_json['username'];
		this.logged = true;
	}

	async get_party_owner(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/party/${this.party_id}`, {
			method: 'GET',
			credentials: 'include'
		});
		if (response.status !== 200)
			return ;
		const response_json = await response.json();
		this.owner = response_json['owner'];
	}
};

class Player {
	state: PlayState = $state(PlayState.PAUSED);
};

export function setUser(): User {
	return setContext<User>(USER_KEY, new User());
}

export function getUser(): User {
	return getContext<User>(USER_KEY);
}

export function setPlayer(): Player {
	return setContext<Player>(PLAYER_KEY, new Player());
}

export function getPlayer(): Player {
	return getContext<Player>(PLAYER_KEY);
}
