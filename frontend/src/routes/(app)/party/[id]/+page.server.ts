import env from "$lib/env";

export async function load({ cookies }) {
	const cookie_string: string = `access_token=${cookies.get('access_token')}`;
	const response = await fetch(env.SERVER_BACKEND_URL + '/song', {
		method: 'GET',
		headers: {
			Cookie: cookie_string,
		},
	});
	if (response.status !== 200)
		return ;
	return { 'songs': await response.json() };
}
