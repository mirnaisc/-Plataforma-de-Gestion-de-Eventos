"""Initial migration

Revision ID: 45bd4d115b87
Revises: 
Create Date: 2024-07-13 17:29:29.768561

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '45bd4d115b87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Eliminar restricciones de claves foráneas
    op.drop_constraint('notificaciones_usuario_id_fkey', 'notificaciones', type_='foreignkey')
    op.drop_constraint('notificaciones_evento_id_fkey', 'notificaciones', type_='foreignkey')
    op.drop_constraint('registros_eventos_usuario_id_fkey', 'registros_eventos', type_='foreignkey')
    op.drop_constraint('registros_eventos_evento_id_fkey', 'registros_eventos', type_='foreignkey')
    op.drop_constraint('eventos_organizador_id_fkey', 'eventos', type_='foreignkey')
    op.drop_constraint('usuarios_role_id_fkey', 'usuarios', type_='foreignkey')

    # Eliminar las tablas
    op.drop_table('notificaciones')
    op.drop_table('registros_eventos')
    op.drop_table('eventos')
    op.drop_table('usuarios')
    op.drop_table('roles')


def downgrade():
    # Restaurar las tablas
    op.create_table('roles',
    sa.Column('role_id', sa.INTEGER(), server_default=sa.text("nextval('roles_role_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('role_nombre', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('role_id', name='roles_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('usuarios',
    sa.Column('usuario_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('correo', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('contraseña', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('foto_perfil', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fecha_creacion', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], name='usuarios_role_id_fkey'),
    sa.PrimaryKeyConstraint('usuario_id', name='usuarios_pkey'),
    sa.UniqueConstraint('correo', name='usuarios_correo_key')
    )
    op.create_table('eventos',
    sa.Column('evento_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('descripcion', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('fecha', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('hora', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('lugar', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('capacidad_maxima', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('organizador_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fecha_creacion', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['organizador_id'], ['usuarios.usuario_id'], name='eventos_organizador_id_fkey'),
    sa.PrimaryKeyConstraint('evento_id', name='eventos_pkey')
    )
    op.create_table('registros_eventos',
    sa.Column('registro_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('usuario_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('evento_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fecha_registro', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['evento_id'], ['eventos.evento_id'], name='registros_eventos_evento_id_fkey'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.usuario_id'], name='registros_eventos_usuario_id_fkey'),
    sa.PrimaryKeyConstraint('registro_id', name='registros_eventos_pkey'),
    sa.UniqueConstraint('usuario_id', 'evento_id', name='registros_eventos_usuario_id_evento_id_key')
    )
    op.create_table('notificaciones',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('usuario_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('evento_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('mensaje', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('fecha_envio', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['evento_id'], ['eventos.evento_id'], name='notificaciones_evento_id_fkey'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.usuario_id'], name='notificaciones_usuario_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='notificaciones_pkey')
    )

    # Restaurar restricciones de claves foráneas
    op.create_foreign_key('notificaciones_usuario_id_fkey', 'notificaciones', 'usuarios', ['usuario_id'], ['usuario_id'])
    op.create_foreign_key('notificaciones_evento_id_fkey', 'notificaciones', 'eventos', ['evento_id'], ['evento_id'])
    op.create_foreign_key('registros_eventos_usuario_id_fkey', 'registros_eventos', 'usuarios', ['usuario_id'], ['usuario_id'])
    op.create_foreign_key('registros_eventos_evento_id_fkey', 'registros_eventos', 'eventos', ['evento_id'], ['evento_id'])
    op.create_foreign_key('eventos_organizador_id_fkey', 'eventos', 'usuarios', ['organizador_id'], ['usuario_id'])
