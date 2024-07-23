<script lang="ts">
	async function login(service: string): Promise<void> {
		const response = await fetch(`http://192.168.1.154:3000/login/${service}`);
		if (response.status != 200)
			return ; //Should display a notification
		const url: string = (await response.json())['url'];
	    	window.location = url;
	}
</script>

<h2>login</h2>
<button on:click={() => login('spotify')}>Spotify</button>
<button on:click={() => login('deezer')}>Deezer</button>
