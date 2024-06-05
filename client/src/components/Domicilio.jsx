import { getDomiciliarios, getPedido } from "./API/Conexion-api";
import React, { useEffect, useState } from "react";

function Domicilio({ session }) {
  const [correct, setCorrect] = useState(null);
  const [domicilio, setDomicilio] = useState(null);

  useEffect(() => {
    const fetchDomiciliarios = async () => {
      try {
        const domiciliarios = await getDomiciliarios(session.user.email);
        setCorrect(domiciliarios.data);
      } catch (error) {
        console.error("Error fetching domiciliarios:", error);
      }
    };
    fetchDomiciliarios();
  }, [session]);

  const handleDomicilio = async () => {
    if (correct.activo === true) {
      try {
        const pedido = await getPedido(session.user.email);
        setDomicilio(pedido.data);
      } catch (error) {
        console.error("Error fetching pedido:", error);
      }
    }
  };

  return (
    <section className="min-h-screen flex flex-col items-center justify-center bg-vinotinto text-white p-8">
      {correct ? (
        <section className="w-full max-w-3xl bg-white rounded-lg shadow-lg p-6 text-black">
          <h1 className="text-2xl font-bold mb-4">
            ¡Hola! {session.user.email}, eres un repartidor activo, puedes
            revisar tus pedidos
          </h1>
          <button
            onClick={handleDomicilio}
            className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
          >
            Ver pedidos
          </button>
          {domicilio && (
            <section>
              <h2 className="text-xl font-semibold mb-2">Pedidos</h2>
              <p className="mb-4">Dirección: {domicilio.direccion}</p>
              {domicilio.productos.map((producto, index) => (
                <section
                  key={index}
                  className="bg-gray-100 rounded-lg p-4 mb-4"
                >
                  <h3 className="text-lg font-semibold">Producto {index + 1}</h3>
                  <p>ID: {producto.id}</p>
                  <p>Cantidad: {producto.cantidad}</p>
                  <p>Carrito: {producto.carrito}</p>
                  <p>Producto: {producto.producto}</p>
                </section>
              ))}
            </section>
          )}
        </section>
      ) : (
        <h1 className="text-2xl font-bold">
          ¡Hola! Recuerda que este es un sitio solo para repartidores, inicia
          sesión con una cuenta de repartidor.
        </h1>
      )}
    </section>
  );
}

export default Domicilio;
