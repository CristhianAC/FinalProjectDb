import { getDomiciliarios, getPedido, activar, entregar } from "./API/Conexion-api";
import React, { useEffect, useState } from "react";

function Domicilio({ session }) {
  const [correct, setCorrect] = useState(null);
  const [domicilio, setDomicilio] = useState(null);
  const [solicitado, setSolicitado] = useState(false);

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
    } else {
      await activar(session.user.email);
      try {
        const pedido = await getPedido(session.user.email);
        setDomicilio(pedido.data);
      } catch (error) {
        console.error("Error fetching pedido:", error);
      }
    }
    setSolicitado(true);
    if(!domicilio.productos){
      window.location.reload();
    }
  };
  const handleEntregado = async () => {
    try {
      await entregar(session.user.email);
      window.location.reload();
    } catch (error) {
      console.error("Error entregando pedido:", error);
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
          {domicilio && correct.activo === true && solicitado === true ? (
            <section>
              <h2 className="text-xl font-semibold mb-2">Pedidos</h2>
              <p className="mb-4">Dirección: {domicilio.direccion}</p>
              <p className="mb-4">Total: ${domicilio.total} COP</p>
              {Object.entries(domicilio.productos).map(([nombre, producto], index) => (
                <section
                  key={index}
                  className="bg-gray-100 rounded-lg p-4 mb-4"
                >
                  <h3 className="text-lg font-semibold">Producto {index + 1}</h3>
                  <p>Nombre: {nombre}</p>
                  <p>Precio: ${producto.precio} COP</p>
                  <p>Cantidad: {producto.cantidad}</p>
                  <p>Total: ${producto.total} COP</p>
                </section>
                
              ))}
              <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4" onClick={handleEntregado}>Marcar como entregado</button>
            </section>
          ) : (
            <h4 >No tienes pedidos a cargo</h4>
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
