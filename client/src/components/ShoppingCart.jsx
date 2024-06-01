import { Link } from "react-router-dom";
import CartItems from "./CartItems";

const ShoppingC = ({ cart }) => {
  // Ensure cart is defined and is an array
  const shoppingCart = cart || [];

  return (
    <div className="shopping-cart-container">
      <button className="m-10 bg-[#f7f3e9] text-[#310e11] p-3 hover:bg-[#aca9a3] transition-all duration-500 rounded-2xl">
        <Link to="/productos/" className="">
          <i className="fas fa-arrow-left mr-2"></i>
          <span>Productos</span>
        </Link>
      </button>
      <h2>Carrito</h2>
      <div>
        <CartItems carrito={shoppingCart} />
      </div>
    </div>
  );
};

export default ShoppingC;
