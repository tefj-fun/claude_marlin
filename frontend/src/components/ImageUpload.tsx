import React from 'react';
import { useMutation } from 'react-query';
import { uploadImage } from '../services/api';
import { Detection } from '../types/detection';

interface Props {
  onDetections: (d: Detection[]) => void;
}

const ImageUpload: React.FC<Props> = ({ onDetections }) => {
  const mutation = useMutation(uploadImage, {
    onSuccess: (data) => onDetections(data.detections as Detection[]),
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const formData = new FormData();
      formData.append('image', file);
      mutation.mutate(formData);
    }
  };

  return <input type="file" onChange={handleChange} />;
};

export default ImageUpload;
