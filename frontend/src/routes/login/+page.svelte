<script lang="ts">
	import env from "$lib/env";

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
<button onclick={() => login("spotify")}>Spotify</button>
<button onclick={() => login("deezer")}>Deezer</button>
