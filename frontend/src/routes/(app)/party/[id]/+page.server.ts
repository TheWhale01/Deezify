import { error } from "@sveltejs/kit";
import type Party from "$lib/types/party";
import env from "$lib/env";
import type SearchResult from "$lib/types/search_results";

export async function load({ params, cookies }: any): Promise<Party> {
	// Check if the requested id exists
	// if not display 404
	// else return the party obj
	const cookie_string: string = `access_token=${cookies.get("access_token")}`;
	const response = await fetch(env.SERVER_BACKEND_URL + `/party/${params.id}`, {
		method: "GET",
		headers: {
			Cookie: cookie_string,
		},
	});
	if (response.status !== 200) throw error(404);
	const response_json = await response.json();
	return {
		id: response_json["id"],
		name: response_json["name"],
		owner_id: response_json["owner_id"],
	};
}

export const actions = {
	default: async({ cookies, request }: any): Promise<SearchResult[]> => {
		const data = await request.formData();
		const query: string = data.get('search');
		const cookie_string: string = `access_token=${cookies.get('access_token')}`;
		const response = await fetch(env.SERVER_BACKEND_URL + `/search?q=${query}`, {
			method: 'GET',
			headers: {
				Cookie: cookie_string
			},
		});

		if (response.status !== 200)
			throw error(response.status);
		return await response.json();
	},
};
