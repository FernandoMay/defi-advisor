use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder};
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
struct UserRiskProfile {
    user_address: String,
    risk_profile: u8,
}

#[derive(Serialize)]
struct Recommendation {
    strategy_id: String,
    description: String,
}

#[get("/hello")]
async fn hello() -> impl Responder {
    HttpResponse::Ok().body("Hello world!")
}

#[post("/risk_profile")]
async fn set_risk_profile(info: web::Json<UserRiskProfile>) -> impl Responder {
    // Aquí se integraría la lógica para interactuar con el contrato inteligente
    // o una base de datos para almacenar el perfil de riesgo.
    println!("Received risk profile for {}: {}", info.user_address, info.risk_profile);
    HttpResponse::Ok().json(info.0)
}

#[get("/recommendations/{user_address}")]
async fn get_recommendations(path: web::Path<String>) -> impl Responder {
    let user_address = path.into_inner();
    // Aquí se integraría la lógica para llamar al módulo de IA y obtener recomendaciones.
    let recommendations = vec![
        Recommendation { strategy_id: "STG001".to_string(), description: "Staking en protocolo X".to_string() },
        Recommendation { strategy_id: "STG002".to_string(), description: "Yield farming en protocolo Y".to_string() },
    ];
    HttpResponse::Ok().json(recommendations)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "actix_web=info");
    env_logger::init();

    HttpServer::new(|| {
        App::new()
            .service(hello)
            .service(set_risk_profile)
            .service(get_recommendations)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
