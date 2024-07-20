<script lang="ts">
    import { goto } from "$app/navigation";

	async function sp_login(): Promise<void> {
		const response = await fetch('http://192.168.1.154:3000/login/spotify');
		if (response.status != 200)
			return ; //Should display a notification
		const url: string = (await response.json())['url'];
	    	window.location = url
	}
</script>

<h2>login</h2>
<button on:click={sp_login}>Spotify</button>
