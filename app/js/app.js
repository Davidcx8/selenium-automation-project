// app.js - Lógica principal de la aplicación CRUD

// Clase para gestionar registros
class RecordManager {
    constructor() {
        this.records = this.loadRecords();
        this.currentRecordId = null;
        this.initializeElements();
        this.attachEventListeners();
        this.checkAuthentication();
        this.renderTable();
    }

    /**
     * Inicializa elementos del DOM
     */
    initializeElements() {
        // Botones principales
        this.btnNewRecord = document.getElementById('btn-new-record');
        this.btnLogout = document.getElementById('btn-logout');
        this.btnSave = document.getElementById('btn-save');
        this.btnCancel = document.getElementById('btn-cancel');
        this.btnCancelDelete = document.getElementById('btn-cancel-delete');
        this.btnConfirmDelete = document.getElementById('btn-confirm-delete');

        // Modales
        this.recordModal = document.getElementById('record-modal');
        this.deleteModal = document.getElementById('delete-modal');

        // Formulario
        this.recordForm = document.getElementById('record-form');
        this.recordIdInput = document.getElementById('record-id');
        this.recordNameInput = document.getElementById('record-name');
        this.recordDescriptionInput = document.getElementById('record-description');
        this.recordCategoryInput = document.getElementById('record-category');
        this.recordDateInput = document.getElementById('record-date');

        // Tabla
        this.tableBody = document.getElementById('table-body');
        this.emptyState = document.getElementById('empty-state');
        this.totalCount = document.getElementById('total-count');

        // Alerta
        this.alertContainer = document.getElementById('alert-container');
        this.alertMessage = document.getElementById('alert-message');

        // Usuario actual
        this.currentUserSpan = document.getElementById('current-user');

        // Modal title
        this.modalTitle = document.getElementById('modal-title');
    }

    /**
     * Adjunta event listeners
     */
    attachEventListeners() {
        this.btnNewRecord.addEventListener('click', () => this.openCreateModal());
        this.btnLogout.addEventListener('click', () => this.logout());
        this.btnCancel.addEventListener('click', () => this.closeRecordModal());
        this.btnCancelDelete.addEventListener('click', () => this.closeDeleteModal());
        this.btnConfirmDelete.addEventListener('click', () => this.confirmDelete());
        this.recordForm.addEventListener('submit', (e) => this.handleSubmit(e));

        // Cerrar modales al hacer clic fuera
        this.recordModal.addEventListener('click', (e) => {
            if (e.target === this.recordModal) {
                this.closeRecordModal();
            }
        });

        this.deleteModal.addEventListener('click', (e) => {
            if (e.target === this.deleteModal) {
                this.closeDeleteModal();
            }
        });
    }

    /**
     * Verifica autenticación
     */
    checkAuthentication() {
        const isAuthenticated = sessionStorage.getItem('isAuthenticated');
        if (isAuthenticated !== 'true') {
            window.location.href = 'login.html';
            return;
        }

        const currentUser = sessionStorage.getItem('currentUser') || 'Usuario';
        this.currentUserSpan.textContent = currentUser;
    }

    /**
     * Carga registros desde localStorage
     */
    loadRecords() {
        const stored = localStorage.getItem('records');
        return stored ? JSON.parse(stored) : [];
    }

    /**
     * Guarda registros en localStorage
     */
    saveRecords() {
        localStorage.setItem('records', JSON.stringify(this.records));
    }

    /**
     * Genera un ID único
     */
    generateId() {
        return Date.now().toString();
    }

    /**
     * Renderiza la tabla de registros
     */
    renderTable() {
        this.tableBody.innerHTML = '';

        if (this.records.length === 0) {
            this.emptyState.classList.remove('hidden');
            this.totalCount.textContent = '0';
            return;
        }

        this.emptyState.classList.add('hidden');

        // Ordenar por ID (más reciente primero)
        const sortedRecords = [...this.records].sort((a, b) => b.id - a.id);

        sortedRecords.forEach(record => {
            const row = this.createTableRow(record);
            this.tableBody.appendChild(row);
        });

        this.totalCount.textContent = this.records.length;
    }

    /**
     * Crea una fila de tabla
     */
    createTableRow(record) {
        const tr = document.createElement('tr');
        tr.setAttribute('data-id', record.id);

        tr.innerHTML = `
            <td>${record.id}</td>
            <td>${this.escapeHtml(record.name)}</td>
            <td>${this.escapeHtml(record.description) || '-'}</td>
            <td>${this.escapeHtml(record.category) || '-'}</td>
            <td>${record.date || '-'}</td>
            <td class="table-actions">
                <button class="btn btn-secondary btn-sm btn-edit" data-id="${record.id}">
                    ✏️ Editar
                </button>
                <button class="btn btn-danger btn-sm btn-delete" data-id="${record.id}">
                    🗑️ Eliminar
                </button>
            </td>
        `;

        // Event listeners para botones
        const btnEdit = tr.querySelector('.btn-edit');
        const btnDelete = tr.querySelector('.btn-delete');

        btnEdit.addEventListener('click', () => this.openEditModal(record.id));
        btnDelete.addEventListener('click', () => this.openDeleteModal(record.id));

        return tr;
    }

    /**
     * Escapa HTML para prevenir XSS
     */
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Abre modal para crear registro
     */
    openCreateModal() {
        this.modalTitle.textContent = 'Nuevo Registro';
        this.recordForm.reset();
        this.recordIdInput.value = '';
        this.currentRecordId = null;

        // Establecer fecha actual por defecto
        const today = new Date().toISOString().split('T')[0];
        this.recordDateInput.value = today;

        this.recordModal.classList.add('show');
        this.recordNameInput.focus();
    }

    /**
     * Abre modal para editar registro
     */
    openEditModal(id) {
        const record = this.records.find(r => r.id === id);
        if (!record) return;

        this.modalTitle.textContent = 'Editar Registro';
        this.recordIdInput.value = record.id;
        this.recordNameInput.value = record.name;
        this.recordDescriptionInput.value = record.description || '';
        this.recordCategoryInput.value = record.category || '';
        this.recordDateInput.value = record.date || '';

        this.currentRecordId = id;
        this.recordModal.classList.add('show');
        this.recordNameInput.focus();
    }

    /**
     * Cierra modal de registro
     */
    closeRecordModal() {
        this.recordModal.classList.remove('show');
        this.recordForm.reset();
        this.currentRecordId = null;
    }

    /**
     * Abre modal de confirmación para eliminar
     */
    openDeleteModal(id) {
        this.currentRecordId = id;
        this.deleteModal.classList.add('show');
    }

    /**
     * Cierra modal de confirmación para eliminar
     */
    closeDeleteModal() {
        this.deleteModal.classList.remove('show');
        this.currentRecordId = null;
    }

    /**
     * Maneja el submit del formulario
     */
    handleSubmit(event) {
        event.preventDefault();

        const name = this.recordNameInput.value.trim();
        const description = this.recordDescriptionInput.value.trim();
        const category = this.recordCategoryInput.value;
        const date = this.recordDateInput.value;

        // Validar campo obligatorio
        if (!name) {
            this.showAlert('El nombre es obligatorio', 'error');
            this.recordNameInput.focus();
            return;
        }

        // Validar longitud del nombre
        if (name.length > 100) {
            this.showAlert('El nombre no puede tener más de 100 caracteres', 'error');
            this.recordNameInput.focus();
            return;
        }

        // Validar longitud de descripción
        if (description.length > 500) {
            this.showAlert('La descripción no puede tener más de 500 caracteres', 'error');
            this.recordDescriptionInput.focus();
            return;
        }

        // Validar fecha futura
        if (date) {
            const selectedDate = new Date(date);
            const today = new Date();
            today.setHours(0, 0, 0, 0);

            if (selectedDate > today) {
                const confirmFuture = confirm('La fecha seleccionada es futura. ¿Desea continuar?');
                if (!confirmFuture) {
                    return;
                }
            }
        }

        if (this.currentRecordId) {
            // Actualizar registro existente
            this.updateRecord(this.currentRecordId, { name, description, category, date });
        } else {
            // Crear nuevo registro
            this.createRecord({ name, description, category, date });
        }
    }

    /**
     * Crea un nuevo registro
     */
    createRecord(data) {
        const newRecord = {
            id: this.generateId(),
            name: data.name,
            description: data.description,
            category: data.category,
            date: data.date,
            createdAt: new Date().toISOString()
        };

        this.records.push(newRecord);
        this.saveRecords();
        this.renderTable();
        this.closeRecordModal();
        this.showAlert('Registro creado exitosamente', 'success');
    }

    /**
     * Actualiza un registro existente
     */
    updateRecord(id, data) {
        const index = this.records.findIndex(r => r.id === id);
        if (index === -1) return;

        this.records[index] = {
            ...this.records[index],
            name: data.name,
            description: data.description,
            category: data.category,
            date: data.date,
            updatedAt: new Date().toISOString()
        };

        this.saveRecords();
        this.renderTable();
        this.closeRecordModal();
        this.showAlert('Registro actualizado exitosamente', 'success');
    }

    /**
     * Confirma y ejecuta la eliminación
     */
    confirmDelete() {
        if (!this.currentRecordId) return;

        this.records = this.records.filter(r => r.id !== this.currentRecordId);
        this.saveRecords();
        this.renderTable();
        this.closeDeleteModal();
        this.showAlert('Registro eliminado exitosamente', 'success');
    }

    /**
     * Muestra una alerta
     */
    showAlert(message, type = 'success') {
        this.alertMessage.textContent = message;
        this.alertContainer.className = `alert alert-${type} show`;

        setTimeout(() => {
            this.alertContainer.classList.remove('show');
        }, 5000);
    }

    /**
     * Cierra sesión
     */
    logout() {
        sessionStorage.clear();
        window.location.href = 'login.html';
    }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    new RecordManager();
});
