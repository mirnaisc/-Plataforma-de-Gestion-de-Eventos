<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Plataforma de Eventos</title>
  <link href="https://unpkg.com/tailwindcss@^2.0/dist/tailwind.min.css" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css"> 
</head>
<body>
  <header class="bg-yellow-800 text-white">
    <nav class="container mx-auto px-4 py-2 flex justify-between items-center">
      <ul class="flex space-x-4">
        <li><a href="dashboard.php" class="hover:text-gray-400">Inicio</a></li>
        <li><a href="eventos.php" class="hover:text-gray-400">Eventos</a></li>
        <?php if (isset($_SESSION['user_id'])): ?>
          <li><a href="perfil.php" class="hover:text-gray-400">Perfil</a></li>
          <?php if ($_SESSION['rol'] == 'organizador' || $_SESSION['rol'] == 'ambos'): ?>
            <li><a href="crear_evento.php" class="hover:text-gray-400">Crear Evento</a></li>
          <?php endif; ?>
          <li><a href="logout.php" class="hover:text-gray-400">Cerrar Sesión</a></li>
        <?php else: ?>
          <li><a href="registro.php" class="hover:text-gray-400">Registrarse</a></li>
          <li><a href="login.php" class="hover:text-gray-400">Iniciar Sesión</a></li>
        <?php endif; ?>
      </ul>
    </nav>
  </header>
  <div class="container mx-auto py-10">
    <!-- Contenido de tu página -->
  </div>
</body>
</html>

<!-- #region -->