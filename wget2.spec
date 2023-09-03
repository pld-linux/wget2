#
# Conditional build:
%bcond_without	tests	# check target
%bcond_with	gnutls	# use GnuTLS (wget default) instead of OpenSSL
%bcond_with	pandoc	# build man with pandoc

Summary:	A utility for retrieving files using the HTTP or FTP protocols
Summary(es.UTF-8):	Cliente en línea de comando para bajar archivos WWW/FTP con recursión opcional
Summary(fr.UTF-8):	Un utilitaire pour recuperer des fichiers en utilisant les protocoles HTTP ou FTP
Summary(pl.UTF-8):	Wsadowy klient HTTP/FTP
Summary(pt_BR.UTF-8):	Cliente na linha de comando para baixar arquivos WWW/FTP com recursão opcional
Summary(ru.UTF-8):	Утилита для получения файлов по протоколам HTTP и FTP
Summary(uk.UTF-8):	Утиліта для отримання файлів по протоколам HTTP та FTP
Summary(zh_CN.UTF-8):	[通讯]功能强大的下载程序,支持断点续传
Name:		wget2
Version:	2.1.0
Release:	1
License:	GPL v3+ with OpenSSL exception
Group:		Networking/Utilities
Source0:	https://ftp.gnu.org/gnu/wget/%{name}-%{version}.tar.lz
# Source0-md5:	0ec2d5738a19967e90e26e3f28f83339
URL:		http://www.gnu.org/software/wget/
BuildRequires:	bzip2-devel
BuildRequires:	doxygen
BuildRequires:	gettext-tools >= 0.21
# >= 3.6.3 for TLSv1.3
%{?with_gnutls:BuildRequires:	gnutls-devel >= 3.0.16}
BuildRequires:	gpgme-devel
BuildRequires:	libbrotli-devel
BuildRequires:	libhsts-devel
BuildRequires:	libidn2-devel >= 0.14.0
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libpsl-devel >= 0.16.0
BuildRequires:	lzlib-devel
BuildRequires:	nghttp2-devel
%{!?with_gnutls:BuildRequires:	openssl-devel >= 1.1.0}
%{?with_pandoc:BuildRequires:	pandoc}
BuildRequires:	pcre2-8-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
Requires:	libwget2 = %{version}-%{release}
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqfiles		%{_bindir}/rmold

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you're logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%description -l es.UTF-8
GNU wget es una herramienta de red para bajar archivos usando HTTP y
FTP. Funciona en modo no interactivo, pudiendo trabajar en background.
Funciona muy bien, incluso en conexiones lentas o inestables, bajando
el archivo hasta que sea completamente recibido.

%description -l fr.UTF-8
GNU Wget est un utilitaire pour récupérer des fichiers qui peut
utiliser indifféremment les protocoles HTTP ou FTP. Parmi les
caractéristiques de Wget, citons la capacité à récupérer des fichiers
en arrière-plan alors que vous n'êtes pas connecté, la récupération
récursive de répertoires, la capacité de récupérer des fichiers en
appliquant un filtre sur le nom ou sur la date, la gestion de Rest
avec les serveurs FTP et de Range avec les serveurs HTTP pour
récupérer des fichiers avec une connexion lente ou instable, le
support des serveurs Proxy... Wget est particulièrement configurable.

%description -l ja.UTF-8
GNU wget は HTTP か FTP プロトコルのどちらかを使用することができる ファイルを取得するユーティリティです。wget
はログアウトしている 間にバックグラウンドで働く特徴をもっていること、ディレクトリの再帰的
取得、ファイルネームのワイルドカードマッチング、ファイルのタイムスタンプの 保存と比較、遅く不安定な接続で FTP サーバの Rest と
HTTP サーバの Range の使用、プロキシーサーバのサポートと設定の容易さを含んだ特徴を もっています。

%description -l pl.UTF-8
Wget jest klientem FTP/HTTP przeznaczonym do ściągania zasobów
wsadowo. Umożliwia ściąganie zasobów z podkatalogami, a także ma opcje
umożliwiające wykonanie lokalnej kopii zasobów (mirror). W razie
niemożności dostania się do zasobów lub gdy połączenie z serwerem
FTP/HTTP zostanie zerwane, może automatycznie ponawiać próby
kopiowania. Jest także dobrze przystosowany do tego, żeby uruchamiać
go jako zadanie z crona.

%description -l pt_BR.UTF-8
O GNU wget é uma ferramenta de rede para baixar arquivos usando HTTP e
FTP. Ele funciona em modo não interativo, podendo trabalhar em
background. Funciona muito bem, mesmo em conexões lentas ou instáveis,
baixando o arquivo até que ele seja completamente recebido.

%description -l ru.UTF-8
GNU Wget - это утилита командной строки для получения файлов по
протоколам FTP и HTTP. Среди возможностей Wget - работа в фоновом
режиме когда вы выходите из системы, рекурсивное извлечение каталогов,
выбор файлов по шаблону, сравнение времени удаленных и локальных
файлов, сохранение времени удаленных файлов при загрузке,
использование REST с FTP серверами и Range с HTTP серверами для
загрузки файлов по медленным или нестабильным каналам, поддержка Proxy
серверов, конфигурируемость.

%description -l uk.UTF-8
GNU Wget - це утиліта командного рядка для отримання файлів по
протоколам FTP та HTTP. Серед можливостей Wget - робота в фоновому
режимі коли ви виходите із системи, рекурсивне отримання каталогів,
вибір файлів по шаблону, порівняння часу віддалених та локальних
файлів, збереження часу віддалених файлів при завантаженні,
використання REST з FTP серверами та Range з HTTP серверами для
завантаження файлів по повільним чи нестабільним каналам, підтримка
Proxy серверів, настроюваність.

%package -n libwget2
Summary:	Library that provides the basic functions needed by a web client
Summary(pl.UTF-8):	Biblioteka udostępniająca podstawowe funkcje klienta WWW
License:	LGPL v3+
Group:		Libraries
%{?with_gnutls:Requires:	gnutls-libs >= 3.0.16}
Requires:	libidn2 >= 0.14.0
Requires:	libpsl >= 0.16.0
%{!?with_gnutls:Requires:	openssl >= 1.1.0}

%description -n libwget2
Library that provides the basic functions needed by a web client.

%description -n libwget2 -l pl.UTF-8
Biblioteka udostępniająca podstawowe funkcje klienta WWW.

%package -n libwget2-devel
Summary:	Header files for wget2 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wget2
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libwget2 = %{version}-%{release}

%description -n libwget2-devel
Header files for wget2 library.

%description -n libwget2-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wget2.

%package -n libwget2-static
Summary:	Static wget2 library
Summary(pl.UTF-8):	Statyczna biblioteka wget2
License:	LGPL v3+
Group:		Development/Libraries
Requires:	libwget2-devel = %{version}-%{release}

%description -n libwget2-static
Static wget2 library.

%description -n libwget2-static -l pl.UTF-8
Statyczna biblioteka wget2.

%prep
%setup -q

%build
%configure \
	LDCONFIG=true \
	--disable-silent-rules \
	--with-bzip2 \
	--with-gpgme \
	--with-libhsts \
	--with-libidn2 \
	--with-libmicrohttpd \
	--with-libnghttp2 \
	--with-libpcre2 \
	--with-libpsl \
	--with-linux-crypto \
	--with-lzma \
	--with-plugin-support \
	--with-ssl%{!?with_gnutls:=openssl} \
	--with-zlib \
	%{nil}
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_bindir}/wget2_noinstall
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwget.la

%if %{without pandoc}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p docs/man/man1/wget2.1 $RPM_BUILD_ROOT%{_mandir}/man1
%endif

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libwget2 -p /sbin/ldconfig
%postun	-n libwget2 -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/wget2
%{_mandir}/man1/wget2.1*

%files -n libwget2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwget.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwget.so.2

%files -n libwget2-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwget.so
%{_includedir}/wget.h
%{_includedir}/wgetver.h
%{_pkgconfigdir}/libwget.pc
%{_mandir}/man3/libwget*.3*

%files -n libwget2-static
%defattr(644,root,root,755)
%{_libdir}/libwget.a
