import React from 'react';
import { Detection } from '../types/detection';

interface Props {
  detections: Detection[];
}

const DetectionResults: React.FC<Props> = ({ detections }) => (
  <ul>
    {detections.map((d, idx) => (
      <li key={idx}>
        {d.label}: {Math.round(d.confidence * 100)}%
      </li>
    ))}
  </ul>
);

export default DetectionResults;
