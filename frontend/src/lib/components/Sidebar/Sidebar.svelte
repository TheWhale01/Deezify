<script lang="ts">
	import logout from "./logout";
	import { goto } from "$app/navigation";
	import delete_party from "./delete_party";
	import generate_invite_link from "./generate_invite_link";
	import { onMount } from "svelte";
	import SidebarButton from "./SidebarButton.svelte";
	import env from "$lib/env";
	import { owner, logged, party } from "$lib/store.svelte";

	let home_url: string = $state('');
	let delete_url: string = $state('');
	let search_url: string = $state('');

	onMount(async () => {
		const url = $state({value: window.location.pathname});
	
		home_url = url.value.replace('/search', '');
		delete_url = url.value.replace('/search', '');
		search_url = window.location.pathname.endsWith('/search') ? url.value : url.value + '/search';
		logged.value = !url.value.startsWith('/login');
		party.value = url.value.startsWith('/party/');
		if (!party.value)
			return ;
		const party_id: number = Number(url.value.replace('/party/', '').replace('/search', ''));
		if (party) {
			const response = await fetch(env.BACKEND_URL + `/party/${party_id}`, {
				method: 'GET',
				credentials: 'include'
			});
			if (response.status !== 200)
				return ;
			owner.value = (await response.json())['owner'];
		}
	});
</script>

<div class="flex flex-col justify-between items-center h-full p-6 bg-slate-200 shadow-lg">
	<h1>Deezify</h1>

	{#if party.value}
		<SidebarButton icon="fa-house" on:click={() => goto(home_url)} />
		<SidebarButton icon="fa-magnifying-glass" on:click={() => goto(search_url)} />
		{#if owner.value}
			<SidebarButton icon="fa-trash" on:click={() => delete_party(delete_url)} />
			<SidebarButton icon="fa-user-plus" on:click={() => generate_invite_link}/>
		{/if}
	{/if}

	{#if logged.value}
		<SidebarButton icon='fa-right-from-bracket' on:click={logout}/>
	{/if }
</div>
