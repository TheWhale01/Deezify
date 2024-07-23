<script lang="ts">
	import env from "$lib/env";
	import { goto } from "$app/navigation";

	async function logout(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/user/logout`, {
			method: "DELETE",
			credentials: "include",
		});
		if (response.status !== 200) return;
		goto("/login");
	}
</script>

<!--
<svelte:head>
	<script src="https://sdk.scdn.co/spotify-player.js"></script>
</svelte:head> -->

<button on:click={logout}>Log Out</button>
<slot></slot>
