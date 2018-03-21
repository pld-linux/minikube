Summary:	Single Node Kubernetes Cluster
Name:		minikube
Version:	0.25.0
Release:	0.1
License:	Apache v2.0
Group:		Applications/System
Source0:	https://github.com/kubernetes/minikube/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://github.com/kubernetes/minikube
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minikube is a tool that makes it easy to run Kubernetes locally.
Minikube runs a single-node Kubernetes cluster inside a VM on your
laptop for users looking to try out Kubernetes or develop with it
day-to-day.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
