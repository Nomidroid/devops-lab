resource "local_file" "hello" {
  filename = "&{path.module}/server-info.txt"
  content  = "Managed by terraform Env: production\n"
}
