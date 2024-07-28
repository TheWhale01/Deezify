<script lang="ts">
	import env from "$lib/env";
	import { goto } from "$app/navigation";

	export let logged: boolean;

	async function logout(): Promise<void> {
		const response = await fetch(env.BACKEND_URL + `/user/logout`, {
			method: "DELETE",
			credentials: "include",
		});
		if (response.status !== 200) return;
		goto("/login");
	}
</script>

<div class="flex flex-col justify-between items-center h-full p-6 bg-slate-200 shadow-lg">
	<h1>Deezify</h1>

	{#if logged}
		<button on:click={logout}>Log Out</button>	
	{/if }
</div>
