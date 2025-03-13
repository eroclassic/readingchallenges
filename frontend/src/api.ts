import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const getBooks = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/books/`);
    return response.data;
  } catch (error) {
    console.error(error);
    return [];
  }
};

export const getChallenges = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/challenges/`);
    return response.data;
  } catch (error) {
    console.error(error);
    return [];
  }
};
