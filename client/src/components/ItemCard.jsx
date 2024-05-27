

const ItemCard = ({ image, name, price, addToCart }) => {
    return (
        <div className='producto'>
                <img src={image} alt={name} />
                <h4>{name}</h4>
                <p>{price} COP</p>
                <button onClick={addToCart} className="btn">Añadir al Carrito</button>
        </div>
    );
};

export default ItemCard;
