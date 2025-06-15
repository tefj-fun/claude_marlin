import axios from 'axios';

export const uploadImage = async (formData: FormData) => {
  const { data } = await axios.post('/detection', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return data;
};
