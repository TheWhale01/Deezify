import type SearchResult from '$lib/types/search_results.js';
import env from '$lib/env.js';
import { error } from '@sveltejs/kit';

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
