use std::sync::{Arc, Mutex};
use pyo3::{prelude::*, types::{PyDict, PyByteArray, PyBytes}};
use std::sync::mpsc::{SyncSender};
use crate::core::data::Message;

#[pyclass]
pub struct AgentCore {
    pub agent_id: Arc<String>,
    pub domain_name: Arc<String>,
    pub publisher: Arc<Mutex<SyncSender<Message>>>,
}

#[pymethods]
impl AgentCore {
    /**
     * Send a message to the agent
     */
    pub fn message<'p>(&self, py: Python<'p>, message: Py<PyAny>) -> PyResult<&'p PyAny> {
        let receiver = message
            .as_ref(py)
            .get_item("receiver")
            .map(|receiver| receiver.to_string());

        let data = message
            .as_ref(py)
            .get_item("data")
            .map(|data| data.to_object(py));

        let outgoing = Arc::clone(&self.publisher);
        let agent_id = Arc::clone(&self.agent_id);
        let domain_name = Arc::clone(&self.domain_name);
        let rx = async_std::task::spawn(async move {
            let outgoing = outgoing.lock().unwrap();
            let msg = Python::with_gil(|py| {
                Message {
                    from: agent_id.to_string(),
                    data: data.unwrap(),
                    receiver: match receiver {
                        Ok(receiver) => Some(receiver),
                        Err(_) => None,
                    },
                    sender: domain_name.to_string(),
                }
            });
            match outgoing.send(msg) {
                Ok(_) => {}
                Err(e) => {
                    println!("Error: {}", e);
                }
            }
        });

        pyo3_asyncio::async_std::future_into_py(py, async move {
            rx.await;
            Ok(Python::with_gil(|py| "ok".to_object(py)))
        })
    }
}