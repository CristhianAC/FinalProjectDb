import ItemManager from "./ItemManager";
import ShoppingCart from "./ShoppingCart";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/productos" element={<Navigate to="/productos/item-manager" replace />} />
        <Route path="/productos/" element={<ItemManager />} />
        <Route path="/productos" element={<Navigate to="/ShoppingC" replace />} />
        <Route path="/ShoppingC" element={<ShoppingCart />} />
      </Routes>
    </Router>
  );
}

export default App;
