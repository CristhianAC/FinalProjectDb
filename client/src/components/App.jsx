import ItemManager from "./ItemManager";
import ShoppingC from "./ShoppingC";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/productos" element={<Navigate to="/productos/item-manager" replace />} />
        <Route path="/productos/" element={<ItemManager />} />
        <Route path="/productos" element={<Navigate to="/ShoppingC" replace />} />
        <Route path="/productos/ShoppingC" element={<ShoppingC />} />
      </Routes>
    </Router>
  );
}

export default App;
