import React, { useState } from 'react';
import ImageUpload from '../components/ImageUpload';
import DetectionResults from '../components/DetectionResults';
import { Detection } from '../types/detection';

const Dashboard = () => {
  const [detections, setDetections] = useState<Detection[]>([]);

  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">PPE Detection</h1>
      <ImageUpload onDetections={setDetections} />
      <DetectionResults detections={detections} />
    </div>
  );
};

export default Dashboard;
