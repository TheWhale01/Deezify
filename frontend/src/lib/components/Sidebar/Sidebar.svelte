<script lang="ts">
	import logout from "./logout";
	import { goto } from "$app/navigation";
	import delete_party from "./delete_party";
	import generate_invite_link from "./generate_invite_link";
	import SidebarButton from "./SidebarButton.svelte";
	import { getUser } from "$lib/store.svelte";
	import { getNotification } from "../Notifier/Notifier.svelte";

	const user = getUser();
	const notifier = getNotification();
</script>

<div class="flex flex-col justify-between items-center h-full p-6 bg-slate-200 shadow-lg">
	<h1>Deezify</h1>

	{#if user.party_id}
		<SidebarButton icon="fa-house" on:click={() => goto(`/party/${user.party_id}`)} />
		<SidebarButton icon="fa-magnifying-glass" on:click={() => goto(`/party/${user.party_id}/search`)} />
		{#if user.owner}
			<SidebarButton icon="fa-trash" on:click={() => delete_party(`/party/${user.party_id}`)} />
			<SidebarButton icon="fa-user-plus" on:click={() => { generate_invite_link(); notifier.add("Party", "ID copied to clipboard", 'success');}}/>
		{/if}
	{/if}

	{#if user.logged}
		<SidebarButton icon='fa-right-from-bracket' on:click={logout}/>
	{/if }
</div>
