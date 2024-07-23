<script lang="ts">
	async function logout(): Promise<void> {
		const response = await fetch("");
		if (response.status !== 200) return;
		// Remove cookie
		// redirect to login
	}
</script>

<svelte:head>
	<script src="https://sdk.scdn.co/spotify-player.js"></script>
</svelte:head>

<button on:click={logout}>Log Out</button>
<slot></slot>
