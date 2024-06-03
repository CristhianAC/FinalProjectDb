import ItemManager from "./ItemManager";
import ShoppingCart from "./ShoppingCart";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

function App({session}) {
  return (
    <Router>
      <Routes>
        <Route path="/productos" element={<Navigate to="/productos/item-manager" replace />} />
        <Route path="/productos/" element={<ItemManager session={session}/>} />
        <Route path="/productos" element={<Navigate to="/ShoppingC" replace />} />
        <Route path="/ShoppingC" element={<ShoppingCart session={session}  />} />
      </Routes>
    </Router>
  );
}

export default App;
