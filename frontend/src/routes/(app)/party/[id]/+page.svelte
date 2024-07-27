<script lang="ts">
	import type Party from "$lib/types/party";
	import env from "$lib/env";
  import { goto } from "$app/navigation";
	export let data: Party;

	async function delete_party(): Promise<void> {
		const response = await fetch(
			env.BACKEND_URL + `/party/${data.id}`,
			{
				method: "DELETE",
				credentials: "include",
			},
		);
		if (response.status !== 200) return;
		goto('/');
	}
</script>

<h2>Party</h2>

<p>id: {data.id}</p>
<p>owner_id: {data.owner_id}</p>
<p>name: {data.name}</p>

<!-- show the delete button if the connected user is the admin of this party -->
<button on:click={delete_party}>Delete</button>
