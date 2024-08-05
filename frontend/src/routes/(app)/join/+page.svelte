<script lang="ts">
	import { goto } from "$app/navigation";
	import env from "$lib/env";

	let party_code: string = '';

	async function join(): Promise<void> {
		const response = await fetch(
		env.BACKEND_URL + `/party/${party_code}/add_user`,
		{
			method: "PUT",
			credentials: 'include'
		});
		if (response.status !== 200) return;
		window.location.reload();
	}
</script>

<h2>Join Party</h2>

<p>Scan QR code</p>
<button>Scan !</button>
<p>or</p>
<form on:submit|preventDefault={join}>
	<label for="party code">Enter party code</label>
	<input type="text" name="party code" bind:value={party_code} />
	<button type="submit">Join !</button>
</form>
