import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Telemetry from './routes/Telemetry';
import Control from './routes/Control';
import "./global.scss";

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/telemetry" element={<Telemetry />} />
        <Route path="/control" element={<Control />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
