<script lang="ts">
	import Sidebar from "$lib/components/Sidebar/Sidebar.svelte";
	import '@fortawesome/fontawesome-free/css/all.min.css'
	import { setUser } from "$lib/store.svelte";
  import Services from "$lib/enums/services";

	const { children } = $props();
	const user = setUser();
</script>

<svelte:head>
	{#if user.owner && user.service === Services.SPOTIFY}
		<script src="https://sdk.scdn.co/spotify-player.js"></script>
	{/if }
</svelte:head>

<Sidebar/>

<div class="flex flex-col flex-1 justify-around items-center overflow-scroll">
	 {@render children()}
</div>
