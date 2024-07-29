<script lang="ts">
	import logout from "./logout";
	import { goto, invalidateAll } from "$app/navigation";
	import delete_party from "./delete_party";
	import generate_invite_link from "./generate_invite_link";
	import { onMount } from "svelte";

	let logged: boolean = $state(false);
	onMount(() => {
		const url = $state({value: window.location.pathname});
		$effect(() => { logged = !url.value.startsWith('/login'); });
	});
</script>

<div class="flex flex-col justify-between items-center h-full p-6 bg-slate-200 shadow-lg">
	<h1>Deezify</h1>

	<!-- {#if $party}
		<button on:click={() => goto('/')}><i class="fa-solid fa-house"></i></button>
		<button on:click={() => goto(window.location + '/search')}><i class="fa-solid fa-magnifying-glass"></i></button>
		{#if $owner}
			<button on:click={delete_party}><i class="fa-solid fa-trash"></i></button>
			<button on:click={generate_invite_link}><i class="fa-solid fa-user-plus"></i></button>
		{/if}
	{/if} -->

	{#if logged}
		<button onclick={logout} >Log Out</button>	
	{/if }
</div>
