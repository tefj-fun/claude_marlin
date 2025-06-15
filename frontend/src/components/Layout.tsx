import React from 'react';
import { Link } from 'react-router-dom';

const Layout: React.FC<{ children: React.ReactNode }> = ({ children }) => (
  <div>
    <nav className="p-4 bg-gray-100">
      <Link to="/" className="mr-4">Dashboard</Link>
      <Link to="/settings">Settings</Link>
    </nav>
    {children}
  </div>
);

export default Layout;
