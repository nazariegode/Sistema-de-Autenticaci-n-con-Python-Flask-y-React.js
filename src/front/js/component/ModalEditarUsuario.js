import React from 'react';
import "../../styles/ModalEditarUsuario.css";

const ModalEditarUsuario = ({ usuarioEditable, handleChangeUsuarioEditable, handleGuardarCambios, setUsuarioEditable }) => (
  <div className="modal">
    <div className="modal-content">
      <h3>Modificar Usuario</h3>
      <input
        type="text"
        name="nombre"
        value={usuarioEditable.nombre}
        onChange={handleChangeUsuarioEditable}
        placeholder="Nombre"
      />
      <input
        type="text"
        name="email"
        value={usuarioEditable.email}
        onChange={handleChangeUsuarioEditable}
        placeholder="Email"
      />
      <input
        type="text"
        name="rut"
        value={usuarioEditable.rut}
        onChange={handleChangeUsuarioEditable}
        placeholder="RUT"
      />
      <input
        type="text"
        name="telefono"
        value={usuarioEditable.telefono}
        onChange={handleChangeUsuarioEditable}
        placeholder="Teléfono"
      />
      <input
        type="text"
        name="direccion"
        value={usuarioEditable.direccion}
        onChange={handleChangeUsuarioEditable}
        placeholder="Dirección"
      />
      <select
        name="rol"
        value={usuarioEditable.rol}
        onChange={handleChangeUsuarioEditable}
      >
        <option value="Repartidor">Repartidor</option>
        <option value="Tienda">Tienda</option>
        <option value="Consumidor">Consumidor</option>
        <option value="Administrador">Administrador</option>
      </select>
      <button onClick={handleGuardarCambios}>Guardar Cambios</button>
      <button onClick={() => setUsuarioEditable(null)}>Cancelar</button>
    </div>
  </div>
);

export default ModalEditarUsuario;
