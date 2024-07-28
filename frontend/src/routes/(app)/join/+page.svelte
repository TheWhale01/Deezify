<script lang="ts">
	let invite_link: string = '';

	function join(): void {
		window.location.href = invite_link;
	}
</script>

<h2>Join Party</h2>

<p>Scan QR code</p>
<button>Scan !</button>
<p>or</p>
<form on:submit={join}>
	<label for="party code">Enter party code</label>
	<input type="text" name="party code" bind:value={invite_link} />
	<button type="submit">Join !</button>
</form>
