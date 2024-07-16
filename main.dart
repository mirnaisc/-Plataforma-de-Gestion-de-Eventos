import 'package:flutter/material.dart';

void main() {
  runApp(const MiApp());
}

class MiApp extends StatelessWidget {
  const MiApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Demo de Inicio de Sesión en Flutter',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
      ),
      home: const PaginaInicioSesion(),
      routes: {
        '/registro': (context) => const PaginaRegistro(),
      },
    );
  }
}

class PaginaInicioSesion extends StatefulWidget {
  const PaginaInicioSesion({Key? key}) : super(key: key);

  @override
  State<PaginaInicioSesion> createState() => _PaginaInicioSesionState();
}

class _PaginaInicioSesionState extends State<PaginaInicioSesion> {
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();

  void _iniciarSesion() {
    if (_formKey.currentState!.validate()) {
      String email = _emailController.text;
      String password = _passwordController.text;

      // Aquí puedes agregar la lógica para autenticar al usuario con un servidor
      // Por ahora, solo mostramos un mensaje de éxito
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Inicio de sesión exitoso para $email')),
      );
    }
  }

  void _irARegistro() {
    Navigator.pushNamed(context, '/registro');
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/fondo.jpg'), // Ruta de tu imagen de fondo
            fit: BoxFit.cover, // Ajustar la imagen para cubrir todo el contenedor
          ),
        ),
        child: Center(
          child: Container(
            padding: const EdgeInsets.all(16.0),
            constraints: BoxConstraints(maxWidth: 400), // Ancho máximo opcional
            decoration: BoxDecoration(
              color: Colors.amber.withOpacity(0.8), // Fondo dorado con opacidad
              borderRadius: BorderRadius.circular(8.0),
            ),
            child: Form(
              key: _formKey,
              child: Column(
                mainAxisSize: MainAxisSize.min,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Center(
                    child: Text(
                      'INICIAR SESIÓN',
                      textAlign: TextAlign.center, // Alineación centrada del texto
                      style: TextStyle(
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                        color: Colors.black, // Texto negro
                      ),
                    ),
                  ),
                  const SizedBox(height: 16.0),
                  TextFormField(
                    controller: _emailController,
                    decoration: const InputDecoration(
                      labelText: 'Correo electrónico',
                      labelStyle: TextStyle(color: Colors.black), // Texto negro
                    ),
                    keyboardType: TextInputType.emailAddress,
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Por favor ingrese su correo electrónico';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 16.0),
                  TextFormField(
                    controller: _passwordController,
                    decoration: const InputDecoration(
                      labelText: 'Contraseña',
                      labelStyle: TextStyle(color: Colors.black), // Texto negro
                    ),
                    obscureText: true,
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Por favor ingrese su contraseña';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 32.0),
                  Center(
                    child: ElevatedButton(
                      onPressed: _iniciarSesion,
                      style: ButtonStyle(
                        backgroundColor: MaterialStateProperty.all(Colors.black), // Fondo negro
                        foregroundColor: MaterialStateProperty.all(Colors.white), // Texto blanco
                      ),
                      child: const Text('Iniciar sesión'),
                    ),
                  ),
                  const SizedBox(height: 8.0),
                  Center(
                    child: TextButton(
                      onPressed: _irARegistro,
                      child: const Text(
                        '¿No tienes cuenta? Regístrate aquí',
                        style: TextStyle(
                          color: Color.fromARGB(255, 12, 12, 12), // Color del texto del botón de registro
                          decoration: TextDecoration.underline,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }
}

class PaginaRegistro extends StatelessWidget {
  const PaginaRegistro({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(''), // Título vacío para ocultar en la barra de navegación
        automaticallyImplyLeading: false, // Evita mostrar el botón de regreso en la barra de navegación
      ),
      body: Container(
        width: double.infinity,
        height: double.infinity,
        decoration: BoxDecoration(
          image: DecorationImage(
            image: AssetImage('assets/fondo2.jpg'), // Ruta de la imagen de fondo2
            fit: BoxFit.cover, // Ajustar la imagen para cubrir todo el contenedor
          ),
        ),
        child: Center(
          child: Container(
            padding: const EdgeInsets.all(16.0),
            constraints: BoxConstraints(maxWidth: 400), // Ancho máximo opcional
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.8), // Fondo negro con opacidad
              borderRadius: BorderRadius.circular(8.0),
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
              Center(
              child: Text(
              'CREAR CUENTA',
              textAlign: TextAlign.center, // Alineación centrada del texto
              style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: Colors.amber, // Texto dorado
              ),
              ),
              ),

                

                const SizedBox(height: 16.0),
                TextFormField(
                  controller: TextEditingController(), // Añadir controlador para correo electrónico
                  decoration: const InputDecoration(
                    labelText: 'Correo electrónico',
                    labelStyle: TextStyle(color: Colors.amber), // Texto dorado
                  ),
                  keyboardType: TextInputType.emailAddress,
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Por favor ingrese su correo electrónico';
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 16.0),
                TextFormField(
                  controller: TextEditingController(), // Añadir controlador para contraseña
                  decoration: const InputDecoration(
                    labelText: 'Contraseña',
                    labelStyle: TextStyle(color: Colors.amber), // Texto dorado
                  ),
                  obscureText: true,
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Por favor ingrese su contraseña';
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 32.0),
                Center(
                  child: ElevatedButton(
                    onPressed: () {
                      // Lógica para registrar al usuario
                    },
                    style: ButtonStyle(
                      backgroundColor: MaterialStateProperty.all(Colors.amber), // Fondo dorado
                      foregroundColor: MaterialStateProperty.all(Colors.black), // Texto negro
                    ),
                    child: const Text('Crear cuenta'),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

