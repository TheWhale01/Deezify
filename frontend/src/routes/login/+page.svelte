<script lang="ts">
	import env from "$lib/env";
	import { sidebar } from "$lib/store";
    	import { onMount } from "svelte";

	onMount(() => $sidebar = false);

	async function login(service: string): Promise<void> {
		const response = await fetch(env.BACKEND_URL + "/login/" + service);
		if (response.status != 200) return; //Should display a notification
		const url: Location | (string & Location) = (await response.json())[
			"url"
		];
		window.location = url;
	}
</script>

<h2>login</h2>
<button on:click={() => login("spotify")}>Spotify</button>
<button on:click={() => login("deezer")}>Deezer</button>
