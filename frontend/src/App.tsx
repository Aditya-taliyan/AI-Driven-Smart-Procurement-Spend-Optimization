import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from 'react-query';
import { Toaster } from 'react-hot-toast';

// Layout Components
import Layout from './components/Layout';
import Sidebar from './components/Sidebar';
import Header from './components/Header';

// Page Components
import Dashboard from './pages/Dashboard';
import Suppliers from './pages/Suppliers';
import Products from './pages/Products';
import PurchaseOrders from './pages/PurchaseOrders';
import Invoices from './pages/Invoices';
import Contracts from './pages/Contracts';
import Analytics from './pages/Analytics';
import Forecasting from './pages/Forecasting';
import Recommendations from './pages/Recommendations';
import Optimization from './pages/Optimization';

// Styles
import './App.css';
import 'tailwindcss/tailwind.css';

// Create a client for React Query
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-gray-50">
          <div className="flex">
            <Sidebar />
            <div className="flex-1 flex flex-col">
              <Header />
              <main className="flex-1 overflow-y-auto">
                <Routes>
                  <Route path="/" element={<Dashboard />} />
                  <Route path="/suppliers" element={<Suppliers />} />
                  <Route path="/products" element={<Products />} />
                  <Route path="/purchase-orders" element={<PurchaseOrders />} />
                  <Route path="/invoices" element={<Invoices />} />
                  <Route path="/contracts" element={<Contracts />} />
                  <Route path="/analytics" element={<Analytics />} />
                  <Route path="/forecasting" element={<Forecasting />} />
                  <Route path="/recommendations" element={<Recommendations />} />
                  <Route path="/optimization" element={<Optimization />} />
                </Routes>
              </main>
            </div>
          </div>
        </div>
        <Toaster
          position="top-right"
          toastOptions={{
            duration: 4000,
            style: {
              background: '#363636',
              color: '#fff',
            },
          }}
        />
      </Router>
    </QueryClientProvider>
  );
}

export default App;
