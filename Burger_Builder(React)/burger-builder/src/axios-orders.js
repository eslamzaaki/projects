import axios from "axios";
const instance = axios.create({
	baseURL: "https://burger-builder-fe68d-default-rtdb.firebaseio.com",
});

export default instance;
