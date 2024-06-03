import { Link } from "react-router-dom";
import CartItems from "./CartItems";
import { useEffect, useState } from "react";
import { getCarrito, getProductDetails } from "./API/Conexion-api";


const ShoppingC = ({ session }) => {
  const [shoppingCart, setShoppingCart] = useState([]);

  useEffect(() => {
    const fetchCart = async () => {
      if (session && session.email) {
        try {
          const cartData = await getCarrito(session.email);
          const productDetails = await Promise.all(
            cartData.productos.map(async (item) => {
              const response = await getProductDetails(item.producto);
              const product = response.data;
              return { ...item, product };
            })
          );
          setShoppingCart(productDetails);
        } catch (error) {
          console.error('Error fetching cart:', error);
        }
      }
    };
    fetchCart();
  }, [session]);

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
