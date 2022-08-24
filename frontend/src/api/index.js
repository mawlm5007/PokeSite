const API_URL = "http://127.0.0.1:8000/api/cards/";

const getCard = {
    //list card information 
    async getInfo() {
        const response = await fetch(API_URL);
        if (response.status === 204) {
            return {
                'Error': 'User not logged in'
            }
        }
        const jsonResponse = await response.json();
        return jsonResponse
    },
}

export default getCard