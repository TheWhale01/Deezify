<script lang="ts">
	import logout from "./logout";
	import { goto } from "$app/navigation";
	import delete_party from "./delete_party";
	import generate_invite_link from "./generate_invite_link";
	import { onMount } from "svelte";
	import SidebarButton from "./SidebarButton.svelte";

	let logged: boolean = $state(false);
	let party: boolean = $state(false);
	let owner: boolean = true;
	let pathname: string = $state('');

	onMount(() => {
		pathname = window.location.pathname;
		const url = $state({value: window.location.pathname});
		logged = !url.value.startsWith('/login');
		party = url.value.startsWith('/party');
	});
</script>

<div class="flex flex-col justify-between items-center h-full p-6 bg-slate-200 shadow-lg">
	<h1>Deezify</h1>

	{#if party}
		<SidebarButton icon="fa-house" on:click={() => goto(pathname.replace('/search', ''))} />
		<SidebarButton icon="fa-magnifying-glass" on:click={() => goto(window.location + '/search')} />
		{#if owner}
			<SidebarButton icon="fa-trash" on:click={() => delete_party(pathname.replace('/search', ''))} />
			<SidebarButton icon="fa-user-plus" on:click={() => generate_invite_link}/>
		{/if}
	{/if}

	{#if logged}
		<SidebarButton icon='fa-right-from-bracket' on:click={logout}/>
	{/if }
</div>
