export default interface Notification {
	id: string;
	title: string;
	message: string;
	type: 'success' | 'error' | 'info';
};
