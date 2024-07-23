<script lang="ts">
	let party_id: string = '';	
	
	async function join_party(): Promise<void> {
		console.log(party_id);
		console.log("Joinning party");
	}
</script>

<h2>Join Party</h2>

<p>Scan QR code</p>
<button>Scan !</button>
<p>or</p>
<form method="POST" on:submit|preventDefault={join_party}>
	<label for="party code">Enter party code</label>
	<input type="text" name="party code" bind:value={party_id} />
	<button type="submit">Join !</button>
</form>
