INSERT INTO users (id, name, email, password_hash, pfp, is_becado, state) VALUES 
(1,'Karl Marx','marx@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=1',TRUE,'active'),
(2,'Friedrich Nietzsche','nietzsche@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=2',TRUE,'active'),
(3,'Sigmund Freud','freud@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=3',TRUE,'active'),
(4,'Niccolo Machiavelli','machiavelli@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=4',FALSE,'banned'),
(5,'Jean Paul Sartre','sartre@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=5',TRUE,'active'),
(6,'Leonardo da Vinci','davinci@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=6',TRUE,'active'),
(7,'Michelangelo','michelangelo@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=7',TRUE,'active'),
(8,'Vincent van Gogh','vangogh@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=8',TRUE,'active'),
(9,'Salvador Dali','dali@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=9',FALSE,'active'),
(10,'Albert Einstein','einstein@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=10',TRUE,'active'),
(11,'Isaac Newton','newton@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=11',TRUE,'active'),
(12,'Nikola Tesla','tesla@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=12',TRUE,'active'),
(13,'Marie Curie','curie@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=13',TRUE,'active'),
(14,'Kanye West','kanye@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=14',TRUE,'active'),
(15,'Elon Musk','elon@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=15',TRUE,'active'),
(16,'Taylor Swift','taylor@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=16',TRUE,'active'),
(17,'Cristiano Ronaldo','cr7@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=17',TRUE,'active'),
(18,'DaVinci.exe','davinci.exe@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=18',TRUE,'active'),
(19,'Einstein_420','einstein420@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=19',TRUE,'active'),
(20,'FreudDebugging','freuddebug@keyinstitute.edu.sv','ab0ec5a139100e2f51ac08360c79a452','https://i.pravatar.cc/150?img=20',TRUE,'active')
ON CONFLICT DO NOTHING;

INSERT INTO subjects (id, name) VALUES 
(1,'Calculo 1'),
(2,'Fisica 1'),
(3,'Programacion 1'),
(4,'Desarrollo Personal'),
(5,'Introduccion a la Ingenieria')
ON CONFLICT DO NOTHING;

INSERT INTO user_subjects (user_id, subject_id) VALUES 
(1,4),(2,4),(3,4),(4,4),(5,4),
(6,5),(7,5),(8,5),(9,5),
(10,2),(11,2),(12,2),(13,2),
(14,3),(15,3),(16,3),
(17,1),(18,3),(19,2),(20,4)
ON CONFLICT DO NOTHING;

INSERT INTO tutor_profiles (user_id, rating, approved_hours) VALUES 
(6,4.8,120),
(10,5.0,200),
(12,4.9,180),
(14,3.5,50),
(17,4.7,90)
ON CONFLICT DO NOTHING;

INSERT INTO contacts (user_id, twitter, whatsapp, phone, instagram) VALUES 
(1,'@marx','123','111','@marx_ig'),
(2,'@nietzsche','123','222','@nietzsche_ig'),
(3,'@freud','123','333','@freud_ig'),
(10,'@einstein','123','444','@einstein_ig'),
(14,'@kanye','123','555','@kanye_ig')
ON CONFLICT DO NOTHING;

INSERT INTO sessions (id, tutor_id, subject_id, topic, start_time, end_time, tutor_status, description) VALUES 
(1,10,2,'Relativity Basics','2026-01-01 10:00','2026-01-01 11:00','completed','Intro class'),
(2,6,5,'Renaissance Art','2026-01-02 12:00','2026-01-02 13:30','completed','Art history'),
(3,12,2,'Electricity','2026-01-03 14:00','2026-01-03 15:00','pending','Tesla vibes')
ON CONFLICT DO NOTHING;

INSERT INTO session_students (session_id, student_id, student_status) VALUES 
(1,1,'attended'),
(1,2,'attended'),
(2,3,'attended'),
(2,4,'absent'),
(3,5,'pending')
ON CONFLICT DO NOTHING;

INSERT INTO reviews (tutor_id, student_id, rating, comment) VALUES 
(10,1,5,'Mind blowing'),
(6,3,4,'Very artistic'),
(12,5,5,'Electric class'),
(14,2,3,'Kinda chaotic')
ON CONFLICT DO NOTHING;

INSERT INTO tutoring_suggestions
(student_id, tutor_id, subject_id, topic, message, status, created_at)
VALUES

(3,10,2,
'Relativity Help',
'No entiendo los marcos de referencia',
'pending',
'2026-01-05 09:00'),

(5,12,2,
'Electricity and Magnetism',
'Necesito ayuda para el parcial jsjs',
'accepted',
'2026-01-05 10:30'),

(14,6,5,
'Creative Engineering',
'Quiero mezclar arte con ingeniería',
'pending',
'2026-01-05 11:00'),

(17,10,2,
'Physics for Athletes',
'Necesito entender aceleración para una tarea',
'rejected',
'2026-01-05 12:00'),

(19,12,2,
'Tesla Coils',
'bro ocupamos hacer algo épico',
'pending',
'2026-01-05 13:00'),

(18,14,3,
'Frontend Architecture',
'KivyMD me está destruyendo mentalmente',
'pending',
'2026-01-05 14:00'),

(2,20,4,
'Existential Crisis',
'No sé si debuggear tiene sentido',
'accepted',
'2026-01-05 15:00'),

(13,10,2,
'Quantum Curiosity',
'Necesito reforzar teoría antes del laboratorio',
'pending',
'2026-01-05 16:00'),

(7,6,5,
'Art Composition',
'Teach me the renaissance secrets',
'cancelled',
'2026-01-05 17:00'),

(15,14,3,
'Startup Backend',
'Hay que escalar microservicios',
'pending',
'2026-01-05 18:00')

ON CONFLICT DO NOTHING;