import env from "$lib/env";

export async function load({ cookies }) {
	const cookie_string: string = `access_token=${cookies.get('access_token')}`;
	const response_song = await fetch(env.SERVER_BACKEND_URL + '/song', {
		method: 'GET',
		headers: {
			Cookie: cookie_string,
		},
	});
	if (response_song.status !== 200)
		return ;
	const response_song_json = await response_song.json();
	return {
		'songs': response_song_json,
	};
}
