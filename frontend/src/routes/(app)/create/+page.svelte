<script lang="ts">
	let partyname: string = '';

	async function create_party(): Promise<void> {
		console.log(partyname);
		console.log('Creating party');
	}
</script>

<h2>Party creation</h2>

<form method='POST' on:submit|preventDefault={create_party}>
	<input type='text' name='partyname' bind:value={partyname} placeholder="Insert the name of your party"/>
	<button type="submit">Create !</button>
</form>
