import { Link } from "react-router-dom";


const ShoppingCart = ({ cart }) => {
  
    return (
      <div>
        <button className='back-to-products'>
          <Link to='/productos/item-manager' className='back-to-products'>
            <i className="fas fa-arrow-left"></i>
            <span>Productos</span>
          </Link>
        </button>


      </div>
    );
  };
  
export default ShoppingCart;