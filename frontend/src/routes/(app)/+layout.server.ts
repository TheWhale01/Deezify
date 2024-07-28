import env from "$lib/env";
import { redirect } from "@sveltejs/kit";

export async function load({ route, cookies }: any) {
	const cookie_string: string = `access_token=${cookies.get('access_token')}`;

	const response = await fetch(env.SERVER_BACKEND_URL + '/user/party', {
		method: "GET",
		headers: {
			Cookie: cookie_string
		},
	});
	if (response.status !== 200) return ;
	let response_json = undefined;
	try {
		response_json = await response.json();
	}
	catch (error) {
		return ;
	}
	if (response_json && !route.id.startsWith('/(app)/party/[id]'))
		throw redirect(302, `/party/${response_json['id']}`);
}
