import React from 'react';
import { NavLink } from 'react-router-dom';

const Sidebar: React.FC = () => {
  const menuItems = [
    { path: '/', label: 'Dashboard', icon: '📊' },
    { path: '/suppliers', label: 'Suppliers', icon: '🏢' },
    { path: '/products', label: 'Products', icon: '📦' },
    { path: '/purchase-orders', label: 'Purchase Orders', icon: '📋' },
    { path: '/invoices', label: 'Invoices', icon: '🧾' },
    { path: '/contracts', label: 'Contracts', icon: '📄' },
    { path: '/analytics', label: 'Analytics', icon: '📈' },
    { path: '/forecasting', label: 'Forecasting', icon: '🔮' },
    { path: '/recommendations', label: 'Recommendations', icon: '💡' },
    { path: '/optimization', label: 'Optimization', icon: '⚡' },
  ];

  return (
    <div className="w-64 bg-white shadow-lg">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-gray-800">Smart Procurement</h1>
      </div>
      <nav className="mt-6">
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `flex items-center px-6 py-3 text-gray-700 hover:bg-gray-100 hover:text-gray-900 transition-colors ${
                isActive ? 'bg-blue-50 text-blue-600 border-r-4 border-blue-600' : ''
              }`
            }
          >
            <span className="mr-3 text-xl">{item.icon}</span>
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>
    </div>
  );
};

export default Sidebar;
