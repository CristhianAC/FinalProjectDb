import ItemManager from "./ItemManager";
import ShoppingCart from "./ShoppingCart";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/productos" element={<Navigate to="/productos/item-manager" replace />} />
        <Route path="/productos/item-manager" element={<ItemManager />} />
        <Route path="/productos" element={<Navigate to="/ShoppingCart" replace />} />
        <Route path="/ShoppingCart" element={<ShoppingCart />} />
      </Routes>
    </Router>
  );
}

export default App;
